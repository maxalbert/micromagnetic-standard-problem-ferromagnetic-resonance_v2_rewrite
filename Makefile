all: unit-tests integration-tests

unit-tests:
	make -C tests/unit_tests/

integration-tests:
	make -C tests/integration_tests/

.PHONY: all unit-tests integration-tests
