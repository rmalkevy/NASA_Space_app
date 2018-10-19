FROM node:10-alpine

ENV APP_HOME /usr/src/app

# Create a directory where our app will be placed
RUN mkdir -p $APP_HOME

# Change directory so that our commands run inside this new directory
WORKDIR $APP_HOME

# Get all the code needed to run the app
ADD . $APP_HOME

# RUN apk update && apk upgrade \
#    && apk add --no-cache git g++ ca-certificates bash yarn \
#    && yarn global add vue-cli
# RUN yarn install
RUN apk update && apk upgrade \
    && apk add --no-cache git g++ ca-certificates bash ncurses \
    && rm /var/cache/apk/* \
    && npm install -g vue-cli nuxt \
    && npm install --no-bin-links

EXPOSE 4000
# CMD yarn run dev
CMD npm run dev
