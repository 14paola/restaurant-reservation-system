<template>
  <div class="card">
    <h2>Cancelar reserva</h2>

    <form @submit.prevent="cancelReservation">
      <input v-model="reservation_code" type="text" placeholder="Código de reserva" required />
      <button type="submit">Cancelar reserva</button>
    </form>

    <div v-if="message" class="message">
      {{ message }}
    </div>

    <div v-if="errorMessage" class="error">
      {{ errorMessage }}
    </div>
  </div>
</template>

<script>
import api from '../services/api'

export default {
  data() {
    return {
      reservation_code: '',
      message: '',
      errorMessage: ''
    }
  },
  methods: {
    async cancelReservation() {
      this.message = ''
      this.errorMessage = ''

      try {
        const response = await api.post('/reservations/cancel/', {
          reservation_code: this.reservation_code
        })

        this.message = response.data.message
      } catch (error) {
        this.errorMessage = error.response?.data?.error || 'Error al cancelar la reserva.'
      }
    }
  }
}
</script>

<style scoped>
.card {
  background: white;
  padding: 24px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,.08);
}

input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 8px;
  margin-bottom: 12px;
}

button {
  padding: 12px 18px;
  border: none;
  border-radius: 8px;
  background: #dc2626;
  color: white;
  cursor: pointer;
}

.message {
  margin-top: 20px;
  color: green;
  font-weight: bold;
}

.error {
  margin-top: 20px;
  color: red;
  font-weight: bold;
}
</style>