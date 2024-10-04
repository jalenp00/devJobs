db = db.getSiblingDB('devJobsDB'); // Switch to the database

db.jobs.insertMany([
  { title: 'Software Engineer', company: 'Tech Corp', location: 'San Francisco' },
  { title: 'Data Scientist', company: 'Data Inc', location: 'New York' },
]);

db.users.insertOne([
  { name: 'user demo', email: 'user', password: 'admin123' },
]);