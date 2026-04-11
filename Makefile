PROJECT_CODE_NAME=azerty_arab


all:
	make generate
	make generateahk
	make logo

logo:
	echo machin
	python icon/makeicons.py
	cp ./icon/icon.ico ./docs/images/logo-azerty-arab.ico

generateahk: ./dist/${PROJECT_CODE_NAME}.ahk
	cp ./dist/${PROJECT_CODE_NAME}.ahk ./ahk
	cp ./icon/icon.ico icon/dull_icon.ico ./ahk
	cat ./ahk/systray_icon_snipet.ahk >> ./ahk/${PROJECT_CODE_NAME}.ahk

generate: ${PROJECT_CODE_NAME}.toml
	kalamine build ${PROJECT_CODE_NAME}.toml
	cp -r dist docs/
