import axios from 'axios';

const API = 'http://localhost:4000/job';

const createJob = async (job: CreateJob) => {
    try {
        const response = await axios.post(API + '/', job);
        return response.data;
    } catch (error) {
        return { error: error };
    }
};

const getAllJobs = async () => {
    try {
        const response = await axios.get(API + '/');
        return response.data;
    } catch (error) {
        return { error: error };
    }
};

export default {
    createJob,
    getAllJobs,
}