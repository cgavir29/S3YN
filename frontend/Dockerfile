# Docker node version
FROM node:13.11.0

# Create app directory
WORKDIR /app

# Move dependencies to workdir
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy everything to container
COPY . .

# Port where it runs
EXPOSE 3000

# Command to run server
CMD [ "npm", "start" ]