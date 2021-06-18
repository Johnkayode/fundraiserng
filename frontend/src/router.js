import { createWebHistory, createRouter } from "vue-router";
import Home from "./components/Home.vue";
import Login from "./components/Login.vue";
// import Register from "./components/Register.vue";

const Dashboard = () => import("./components/Dashboard.vue")

const routes = [
    {
      path: "/",
      name: "home",
      component: Home,
    },
    {
      path: "/login",
      component: Login,
    },
    {
      path: "/dashboard",
      name: "dashboard",
       // lazy-loaded
      component: Dashboard,
    },

    
];

const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  
export default router;