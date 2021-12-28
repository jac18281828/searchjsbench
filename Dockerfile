ARG VERSION=122821
FROM jac18281828/tsdev:${VERSION}

ARG PROJECT=searchjsbench
WORKDIR /workspaces/${PROJECT}

COPY package.json .

RUN npm install

COPY .eslintrc .
COPY tsconfig.json .
COPY tslint.json .
COPY index.ts .
COPY README.md .
COPY data data/
COPY src src/
COPY jsql jsql/

RUN tsc
RUN eslint src/ --ext .ts

#build
CMD npm start
