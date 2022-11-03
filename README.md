# Dependency injection in Python 

In this repository you can find the code and the [presentation](presentation.pdf) of the talk [Inyección de dependencias, fácil!](https://charlas.2022.es.pycon.org/pycones2022/talk/HHM3H7/) from [PyConES 2022](https://2022.es.pycon.org/)

<a href="https://twitter.com/intent/follow?screen_name=panicoenlaxbox">
    <img src="https://img.shields.io/twitter/follow/panicoenlaxbox.svg?label=Follow%20@panicoenlaxbox" alt="Follow @panicoenlaxbox" />
</a>

## Examples

- [src/dependency_injection/dependency_inversion/abstraction_implementation.py](src/dependency_injection/dependency_inversion/abstraction_implementation.py)
- [src/dependency_injection/dependency_inversion](src/dependency_injection/dependency_inversion)
- [src/dependency_injection/abstractions/duck_typing.py](src/dependency_injection/abstractions/duck_typing.py)
- [src/dependency_injection/abstractions/protocol.py](src/dependency_injection/abstractions/protocol.py)
- [src/dependency_injection/benefits/more_implementations.py](src/dependency_injection/benefits/more_implementations.py)
- [src/dependency_injection/benefits/code_smell.py](src/dependency_injection/benefits/code_smell.py)
- [tests/testing/test_monkey_patching.py](tests/testing/test_monkey_patching.py)
- [tests/testing/test_mocking.py](tests/testing/test_mocking.py)
- [src/dependency_injection/pure_di](src/dependency_injection/pure_di)
- [src/dependency_injection/dependency_injector_library/main_with_no_magic.py](src/dependency_injection/dependency_injector_library/main_with_no_magic.py)
- [src/dependency_injection/dependency_injector_library/main_with_magic.py](src/dependency_injection/dependency_injector_library/main_with_magic.py)
- [tests/dependency_injector_library/test_using_container.py](tests/dependency_injector_library/test_using_container.py)
- [src/dependency_injection/interception/decorator.py](src/dependency_injection/interception/decorator.py)
- [src/dependency_injection/interception/decorator_pattern.py](src/dependency_injection/interception/decorator_pattern.py)

# Installation

```commandline
git clone https://github.com/panicoenlaxbox/pycones2022.git
pipenv install --dev
git init
pipenv shell
pre-commit install
pre-commit autoupdate
```

# Useful and related links

- http://principles-wiki.net/principles:dependency_inversion_principle
- https://www.amazon.es/Design-Patterns-Object-Oriented-professional-computing/dp/0201633612
- https://opensource.com/article/17/5/30-best-practices-software-development-and-testing
- https://github.com/getsentry/responses 
- https://github.com/spulec/freezegun 
- https://github.com/jmcgeheeiv/pyfakefs/
- https://blog.ploeh.dk/2014/06/10/pure-di/
- https://www.manning.com/books/dependency-injection-in-dot-net
- https://python-dependency-injector.ets-labs.org/
- https://github.com/ets-labs/python-dependency-injector/issues/339#issuecomment-747820448
- https://blog.ploeh.dk/2010/02/03/ServiceLocatorisanAnti-Pattern/
- https://peps.python.org/pep-0544/
