#!/usr/bin/env bash

VERSION=$(date +%m%d%y)

docker build . -t searchjsbench:${VERSION} && \
	docker run --rm -i -t searchjsbench:${VERSION}
