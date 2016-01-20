OOMMF_DATA_DIR = micromagnetic_simulation_data/generated_data/oommf
OUTPUT_FILENAMES = dynamic_txyz.txt mxs.npy mys.npy mzs.npy

OOMMF_OUTPUT_FILES = $(foreach filename,$(OUTPUT_FILENAMES),$(OOMMF_DATA_DIR)/$(filename) )


all: unit-tests integration-tests

unit-tests:
	make -C tests/unit_tests/

integration-tests:
	make -C tests/integration_tests/

generate-oommf-data: $(OOMMF_OUTPUT_FILES)
$(OOMMF_OUTPUT_FILES):
	@echo "Generating OOMMF data... This may take a while."
	cd src/micromagnetic_simulations/oommf/ && ./generate_data.sh

reproduce-figures-from-scratch: generate-oommf-data
	cd src && python reproduce_figures.py

.PHONY: all unit-tests integration-tests generate-oommf-data reproduce-figures-from-scratch
