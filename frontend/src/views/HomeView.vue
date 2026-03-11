<template>
  <div class="card">
    <h2>Crear reserva</h2>

    <form @submit.prevent="submitReservation">
      <div class="grid">
        <input v-model="form.name" type="text" placeholder="Nombre completo" required />
        <input v-model="form.email" type="email" placeholder="Correo electrónico" required />
        <input v-model="form.phone" type="text" placeholder="Teléfono" required />
        <input v-model="form.date" type="date" required />
        <input v-model="form.time" type="time" required />
        <input v-model.number="form.guests" type="number" min="1" placeholder="Cantidad de invitados" required />
      </div>

      <button type="button" @click="checkAvailability">Consultar disponibilidad</button>
      <button type="submit">Crear reserva</button>
    </form>

    <div v-if="availabilityMessage" class="message">
      {{ availabilityMessage }}
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
      form: {
        name: '',
        email: '',
        phone: '',
        date: '',
        time: '',
        guests: 1
      },
      availabilityMessage: '',
      errorMessage: ''
    }
  },
  methods: {
    async checkAvailability() {
      this.availabilityMessage = ''
      this.errorMessage = ''

      try {
        const response = await api.get('/api/reservations/availability/', {
        params: {
          date: this.date,
          time: this.time,
        guests: this.guests
  }
})

        this.availabilityMessage = `Disponible: Mesa ${response.data.table_number} para ${response.data.capacity} personas.`
      } catch (error) {
        this.errorMessage = error.response?.data?.error || 'No hay disponibilidad.'
      }
    },
    async submitReservation() {
      this.availabilityMessage = ''
      this.errorMessage = ''

      try {
        const response = await api.post('/reservations/create/', this.form)

        this.$router.push({
          name: 'success',
          query: {
            code: response.data.reservation_code,
            table: response.data.table_number,
            status: response.data.status
          }
        })
      } catch (error) {
        this.errorMessage = error.response?.data?.error || 'Error al crear la reserva.'
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

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 16px;
}

input {
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

button {
  margin-right: 10px;
  margin-top: 10px;
  padding: 12px 18px;
  border: none;
  border-radius: 8px;
  background: #2563eb;
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