# Bitcoin in Python

This is a dead simple implementstion of the Bitcoin protocol in Python. I'm trying to build another app that lets common accounting software have a bitcoin native interface. But I kept getting tripped up on various aspects of the project because my knowledge of bitcoin is high level. To fix this I decided to write a simple implementation of the bitcoin protocol in python.

I will be following Jimmy Song's book "Programming Bitcoin" and the code in the book is a great reference for this project. However the code in this project will look very different from the book. The reason for that is that I am learning Rust as well, and would like to do a similar project in Rust, but I'm not ready. So instead I will structure the code in this project in a similar way to Rust, following 3 principles:

1. Prefer @dataclasses wherever possible.
2. Type hints everywhere.
3. Prefer immutable data structures.
4. Practice code soundness (unintended states should not be representable).

In addition to code style, I will probably take the chance to practice writing more robust python than is shown in the book (testing, error handling, etc.).
