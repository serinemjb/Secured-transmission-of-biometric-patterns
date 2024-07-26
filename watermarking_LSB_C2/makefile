# Compiler
CC = gcc

# Compiler flags
CFLAGS = -Wall -Wextra

# Executable name
TARGET = watermarking_LSB2

# Source files
SRCS = watermarking_LSB2.c functions.c

# Object files
OBJS = $(SRCS:.c=.o)

# Header files
HEADERS = Finger.h ID.h functions.h

# Default target
all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c $(HEADERS)
	$(CC) $(CFLAGS) -c $< -o $@

# Clean target
clean:
	rm -f $(OBJS) $(TARGET)
