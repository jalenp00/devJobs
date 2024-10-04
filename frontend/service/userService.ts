import axios from 'axios';
import Cookies from 'js-cookie';

const API = 'http://localhost:4000/user';

const createUser = async (user: CreateUser) => {
    try {
        const response = await axios.post(API + '/', user);
        return response.data;
    } catch (error) {
        return { error: error };
    }
};

const getUser = async () => {
    try {
        const token = Cookies.get('token');
        if (!token) {
            return { error: 'No token' };
        }
        const response = await axios.post(API + '/user',{}, {
            withCredentials: true,
        });
        console.log('Response: ' + JSON.stringify(response.data));
        if (response.data.error) {
            return { error: response.data.error };
        }
        return response.data;
    } catch (error) {
        console.log('Error: ' + JSON.stringify(error));
        return { error: error };
    }
};

const login = async (user: UserLogin) => {
    try {
        const response = await axios.post(API + '/login', user);
        return response.data;
    } catch (error) {
        return { error: error };
    }
};

const logout = async () => {
    try {
        const response = await axios.post(API + '/logout',{},{
            withCredentials: true,
        });
        return response.data;
    } catch (error) {
        return { error: error };
    }
}

export default {
    createUser,
    getUser,
    login,
    logout,
}
