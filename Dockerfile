ARG VERSION=111021
FROM jac18281828/tsdev:${VERSION}

ARG PROJECT=searchjsbench
WORKDIR /workspaces/${PROJECT}

COPY .eslintrc .
COPY tsconfig.json .
COPY package.json .
COPY tslint.json .
COPY index.ts .
COPY README.md .
COPY data data/
COPY src src/
COPY jsql jsql/

RUN npm install
RUN npm install eslint -g
RUN npm install @types/node
RUN tsc
RUN eslint src/ --ext .ts

#build
CMD npm start
