import axios from "axios";

const api = axios.create({
  baseURL: "https://restaurant-reservation-system-rzm4.onrender.com/api"
});

export default api;