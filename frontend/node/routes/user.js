import express from 'express';
import axios from 'axios';
import redis from 'redis';

const router = express.Router();

const client = redis.createClient({
  url: 'redis://redis:6379'
});

const API = 'http://backend:8000/user';

client.on('error', (err) => console.error('Redis client error:', err));
client.connect().then(() => console.log('Redis client connected'));

const authenticate = async (req, res, next) => {
  try {
    const sessionId = req.cookies.token;

    if (!sessionId) {
      return res.status(401).json({ error: 'Unauthorized: No token id found.' });
    }

    const redisSessionId = await client.get(sessionId);

    if (!redisSessionId) {
      return res.status(401).json({ error: 'Unauthorized: No token id found.' });
    }

    console.log('Session ID:', sessionId);
    console.log('Redis Session ID:', redisSessionId);

    next();
  } catch (error) {
    console.error('Authentication failed:', error);
    return res.status(401).json({ error: 'Unauthorized' });
  }
};

// Get User
router.post('/user', authenticate, async (req, res) => {
  try {
      const sessionId = req.cookies.token;

      if (!sessionId) {
        return res.status(500).json({ error: 'Fetch user failed: No session id found' });
      }

      const rawUser = await client.get(sessionId);
      
      if (!rawUser) {
        return res.status(500).json({ error: 'Fetch user failed' });
      }

      const user = JSON.parse(rawUser);
      return res.json(user);
    } catch (error) {
      return { error: 'Fetch user failed' };
    }
});

// Create User
router.post('/', async (req, res) => { 
    try {
        const response = await axios.post(API + '/', req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({error: error});
    }
});

// Login
router.post('/login', async (req, res) => {
    try {
        const response = await axios.post(API + '/login', req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({error: error});
    }
});

// Logout
router.post('/logout', async (req, res) => {
  try {
    const sessionId = req.cookies.token;
    if (!sessionId) {
      return res.status(500).json({ error: 'Logout failed: No session id found' });
    }
    const response = await client.del(sessionId);
    if (response === 1) {
      console.log('Session deleted');
      return res.json(response);
    } else {
      console.log('Logout failed');
      return res.status(500).json({ error: 'Logout failed' });
    }
  } catch (error) {
    console.error('Logout failed:', error);
    return res.status(500).json({ error: 'Logout failed' });
  }
});

export default router;