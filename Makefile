main:
	pyi-makespec emulator.py --onefile --collect-all c8
	pyi-makespec c8/assembler.py --onefile
	pyi-makespec c8/disassembler.py --onefile

	pyinstaller emulator.spec
	pyinstaller assembler.spec
	pyinstaller disassembler.spec
	cp -r dist/* .

cleanup:
	rm -rf build
	rm ./assembler.spec ./disassembler.spec ./emulator.spec
	rm -rf dist

