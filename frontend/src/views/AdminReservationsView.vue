<template>
  <div class="card">

    <h2>Panel de reservas - Admin</h2>

    <div v-if="!isLoggedIn" class="login-box">

      <h3>Iniciar sesión</h3>

      <form @submit.prevent="loginAdmin">
        <input v-model="loginForm.username" type="text" placeholder="Usuario admin" required />
        <input v-model="loginForm.password" type="password" placeholder="Contraseña" required />
        <button type="submit">Entrar</button>
      </form>

    </div>

    <div v-else>

      <div class="top-bar">
        <p><strong>Sesión iniciada como admin</strong></p>
        <button class="logout-btn" @click="logout">Cerrar sesión</button>
      </div>

      <div class="filters">
        <input v-model="filters.date" type="date" />
        <select v-model="filters.status">
          <option value="">Todos</option>
          <option value="confirmed">Confirmadas</option>
          <option value="cancelled">Canceladas</option>
        </select>
        <button @click="loadReservations">Filtrar</button>
      </div>

      <table v-if="reservations.length">

        <thead>
          <tr>
            <th>Código</th>
            <th>Nombre</th>
            <th>Fecha</th>
            <th>Hora</th>
            <th>Invitados</th>
            <th>Mesa</th>
            <th>Estado</th>
          </tr>
        </thead>

        <tbody>

          <tr v-for="reservation in reservations" :key="reservation.id">

            <td>{{ reservation.reservation_code }}</td>
            <td>{{ reservation.name }}</td>
            <td>{{ reservation.date }}</td>
            <td>{{ reservation.time }}</td>
            <td>{{ reservation.guests }}</td>
            <td>{{ reservation.table_number }}</td>
            <td>{{ reservation.status }}</td>

          </tr>

        </tbody>

      </table>

      <p v-else>No hay reservas para mostrar.</p>

    </div>

    <div v-if="errorMessage" class="error">
      {{ errorMessage }}
    </div>

  </div>
</template>

<script>

import api from "../services/api"

export default {

data(){

return{

loginForm:{
username:"",
password:""
},

token:localStorage.getItem("admin_token")||"",

reservations:[],

filters:{
date:"",
status:""
},

errorMessage:""

}

},

computed:{
isLoggedIn(){
return !!this.token
}
},

mounted(){

if(this.token){
this.loadReservations()
}

},

methods:{

async loginAdmin(){

this.errorMessage=""

try{

const response = await api.post("/auth/login/",this.loginForm)

this.token=response.data.access

localStorage.setItem("admin_token",this.token)

await this.loadReservations()

}catch(error){

this.errorMessage="Credenciales inválidas."

}

},

async loadReservations(){

this.errorMessage=""

try{

const params={}

if(this.filters.date)params.date=this.filters.date
if(this.filters.status)params.status=this.filters.status

const response = await api.get("/reservations/admin/",{

params,

headers:{
Authorization:`Bearer ${this.token}`
}

})

this.reservations=response.data

}catch(error){

this.errorMessage="No se pudieron cargar las reservas."

}

},

logout(){

this.token=""
this.reservations=[]

localStorage.removeItem("admin_token")

}

}

}

</script>