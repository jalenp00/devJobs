import express, { json } from 'express';
import cors from 'cors';
import cookieParser from 'cookie-parser';

const app = express();
const port = 4000;

// Routes
import userRoutes from './routes/user.js';
import jobRoutes from './routes/job.js'; 

app.use(express.json());

// Connection to Front End
app.use(cors({ origin: 'http://localhost:3000', credentials: true })); 

app.use(cookieParser());

app.use('/user', userRoutes);
app.use('/job', jobRoutes); 

app.listen(port, () => {
  console.log(`Node.js server listening at http://localhost:${port}`);
});