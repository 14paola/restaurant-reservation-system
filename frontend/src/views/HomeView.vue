<template>
  <div class="card">

    <h2>Crear reserva</h2>

    <form @submit.prevent="submitReservation">

      <input
        v-model="form.name"
        placeholder="Nombre"
        required
      />

      <input
        v-model="form.phone"
        placeholder="Teléfono"
        required
      />

      <input
        type="date"
        v-model="form.date"
        required
      />

      <input
        type="time"
        v-model="form.time"
        required
      />

      <input
        type="number"
        v-model.number="form.guests"
        min="1"
        placeholder="Cantidad de invitados"
        required
      />

      <div class="buttons">
        <button type="button" @click="checkAvailability">
          Consultar disponibilidad
        </button>

        <button type="submit">
          Crear reserva
        </button>
      </div>

    </form>

    <p v-if="availabilityMessage" class="success">
      {{ availabilityMessage }}
    </p>

    <p v-if="errorMessage" class="error">
      {{ errorMessage }}
    </p>

  </div>
</template>

<script>

import api from "../services/api"

export default {

data(){

return{

form:{
name:"",
phone:"",
date:"",
time:"",
guests:1
},

availabilityMessage:"",
errorMessage:""

}

},

methods:{

async checkAvailability(){

this.errorMessage=""
this.availabilityMessage=""

try{

const response = await api.get("/reservations/availability/",{
params:{
date:this.form.date,
time:this.form.time,
guests:this.form.guests
}
})

if(response.data.available){

this.availabilityMessage =
`Mesa ${response.data.table_number} disponible para ${response.data.capacity} personas.`

}else{

this.errorMessage = "No hay mesas disponibles."

}

}catch(error){

this.errorMessage =
error.response?.data?.error ||
"Error al consultar disponibilidad."

}

},

async submitReservation(){

this.errorMessage=""
this.availabilityMessage=""

try{

const response = await api.post("/reservations/create/",{

name:this.form.name,
phone:this.form.phone,
date:this.form.date,
time:this.form.time,
guests:this.form.guests

})

this.$router.push({
name:"success",
query:{
code:response.data.reservation_code,
table:response.data.table_number,
status:response.data.status
}
})

}catch(error){

this.errorMessage =
error.response?.data?.error ||
"Error al crear la reserva."

}

}

}

}

</script>

<style scoped>

.card{
background:white;
padding:24px;
border-radius:10px;
box-shadow:0 2px 8px rgba(0,0,0,.08);
max-width:420px;
margin:auto;
}

input{
width:100%;
margin-bottom:12px;
padding:10px;
border:1px solid #ccc;
border-radius:8px;
}

.buttons{
display:flex;
gap:10px;
}

button{
padding:10px 16px;
border:none;
border-radius:8px;
background:#2563eb;
color:white;
cursor:pointer;
}

.error{
color:red;
margin-top:10px;
font-weight:600;
}

.success{
color:green;
margin-top:10px;
font-weight:600;
}

</style>