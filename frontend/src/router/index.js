import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ReservationSuccessView from '../views/ReservationSuccessView.vue'
import CancelReservationView from '../views/CancelReservationView.vue'
import AdminReservationsView from '../views/AdminReservationsView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/success',
    name: 'success',
    component: ReservationSuccessView
  },
  {
    path: '/cancel',
    name: 'cancel',
    component: CancelReservationView
  },
  {
    path: '/admin-reservations',
    name: 'admin-reservations',
    component: AdminReservationsView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router