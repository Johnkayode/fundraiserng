import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'http://localhost:8080/account/';

class UserService {
  
    getUserDashboard() {
      return axios.get(API_URL + 'dashboard/', { headers: authHeader() });
    }
}


export default new UserService();