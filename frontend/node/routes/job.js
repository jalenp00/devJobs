import express from 'express';
import axios from 'axios';
const app = express();

const API = 'http://backend:8000/job';

// Create Job
app.post('/', async (req, res) => {
    try {
        const response = await axios.post(API + '/', req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({error: error});
    }
});

app.get('/', async (req, res) => {
    try {
        const response = await axios.get(API + '/');
        res.json(response.data);
    } catch (error) {
        res.status(500).json({error: error});
    }
});

export default app;