all: unit-tests integration-tests

unit-tests:
	make -C tests/unit_tests/

integration-tests:
	make -C tests/integration_tests/

generate-oommf-data:
	cd src/micromagnetic_simulations/oommf/ && ./generate_data.sh

.PHONY: all unit-tests integration-tests
