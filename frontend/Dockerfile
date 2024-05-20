FROM node:18 AS build

WORKDIR /app

COPY . /app

RUN npm install

RUN npm run build

# Stage 2: Serve the react app using nginx
FROM nginx:alpine

# Copy the build output to the nginx html directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
