# Web Stress Tools

This is a command-line tool for performing stress tests on web servers. It uses different methods to generate load and measure the server's response.

## Usage

```bash
python main.py -i <ip> -p <port> -m <method> [-t <threads>] [-v]
```

## Arguments

- `-i`, `--ip`: The target IP address. This argument is required.
- `-p`, `--port`: The target port. This argument is required.
- `-t`, `--threads`: The number of threads to use for the stress test. This argument is optional, default is 4.
- `-m`, `--method`: The method to use for the stress test. Currently, only 'syn' is supported. This argument is required.
- `-v`, `--verbose`: Enable verbose logging. This argument is optional.

## Methods

- `syn`: This method performs a SYN flood attack. It sends a large number of SYN packets to the target server, causing it to consume resources handling the bogus connections. Right now, this tool doesn't work very well because of the current limitations of threading in python. The maximum bandwidth I have gotten from a single python process is around 1.3mbps using 64 threads.

## Logging

By default, the tool logs at the INFO level. If the `-v` or `--verbose` flag is provided, it logs at the DEBUG level.

## Todo

[ ] Support python 3.13 subinterpreters
[ ] Support more methods like http flood, slowloris, http fast reset, etc.