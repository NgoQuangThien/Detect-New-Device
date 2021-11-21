# KERNEL PROGRAM

## Setup

  Biên dịch chương trình

```
  $ make
```

  Nạp chương trình vào kernel

```
  $ sudo ./xdp_pass_user --dev <interface> --auto-mode --force
```

  Kiểm tra chương trình

```
  $ sudo su
  # cat /sys/kernel/debug/tracing/trace_pipe
```
