import axios from 'axios';

const API_URL = 'http://localhost:8000/account/';


class AuthService{

    register(user){
        return axios.post(API_URL + 'register/', {
            email: user.email,
            first_name: user.first_name,
            last_name: user.last_name,
            password: user.password
        }).then(response => {
            console.log(response.data)
            return response.data
        })
       
    }

    confirm(code){
        return axios.post(API_URL + 'confirm-account/', {
            confirmation_code: code
        }).then(response => {
            console.log(response.data)
            return response.data
        })
    }

    login(user){
        return axios.post(API_URL + 'login/', {
            email: user.email,
            password: user.password
        }).then(response => {
            if(response.data.token){
                localStorage.setItem('user', JSON.stringify(response.data.user))
            }

            console.log('Logged in')
            return response.data
        });
        
    }

    logout(){
        localStorage.removeItem('user');
        console.log('Logged out')
    }

 
}

export default new AuthService();