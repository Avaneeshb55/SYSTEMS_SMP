# Linux Process Memory Layout

## Overview

This project explores how a Linux process is organized in memory using the `/proc` filesystem. A simple C program is written, compiled, and run; while it sleeps, its memory map is inspected via `/proc/<pid>/maps`.

---
## Execution Screenshot

Here is the screenshot of the `/proc/<pid>/maps` output during execution:

![Memory Map Screenshot](Screenshots/output.png)


## Memory Regions Identified

### 1. Text Segment 

This is where the compiled machine code (CPU instructions) of our executable sits. In the map file, it shows up as the first line pointing to our binary path with `r-xp` permissions. The execute permission `x` lets the CPU run the code, while it's kept read-only `r` so the program can't accidentally rewrite its own instructions mid-execution.

### 2. Heap 

This region handles dynamic memory allocation when running functions like malloc() or calloc(). In the `/proc` output, it's explicitly tagged as `[heap]` with read and write `rw-p` permissions. It starts out small at lower addresses and dynamically grows upward toward higher addresses whenever the program needs runtime memory.

---

### 3. Stack 

The stack is loaded at the high end of our virtual address space and grows downward. It holds temporary things like function arguments, call frames, and local variables (like our pid variable).It is labeled explicitly as `[stack]` in the maps output, with read + write (`rw-p`) permissions. The OS handles allocating and clean-up automatically as functions push and pop variables.

---

### 4. Shared Libraries 

This region contains external system code that our program relies on to function. In our output, it shows up as rows pointing to files like `/usr/lib/x86_64-linux-gnu/libc.so.6`. This specific file is the standard C library, which contains the actual code for functions we used, like printf() and sleep().

Instead of compiling all that heavy system code directly into our tiny binary file (which would waste a ton of storage and RAM), the Linux OS maps a single copy of these libraries into our virtual address space at runtime. If ten different programs are running at the same time and all using printf(), they all securely share the same underlying library memory, which is why they are called shared libraries.You'll notice it splits into multiple entries with different permissions—like read/execute `r-xp` for running the library functions, and read/write `rw-p` for handling the library's internal variables.

---


## How to Run

```bash
gcc -o memory_layout memory_layout.c

./memory_layout
```

In a second terminal, while the program is sleeping for 60 seconds:

```bash
# Replace <pid> with the PID printed by the program
cat /proc/<pid>/maps
```

---

## Additional Observations

### vsyscall

While looking through the maps output, you might notice a small region at the very end labeled `[vsyscall]`. This stands for Virtual System Call, and it is an old performance optimization trick used by the Linux kernel. Normally, standard commands like checking the system time would force the CPU to switch back and forth between user mode and kernel mode, which adds overhead and slows things down. To save time, `vsyscall` was designed to let the program run those specific commands directly inside user space without hitting the kernel.

`vsyscall` has a permanent fixed address which served to be a major security flaw .In modern systems, it is replaced by `[vdso]`, and the kernel leaves `[vsyscall]` running in a restricted emulation mode purely for legacy applications .

---
