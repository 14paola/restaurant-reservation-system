<template>

<div class="card">

<h2>Cancelar reserva</h2>

<form @submit.prevent="cancelReservation">

<input
v-model="reservationCode"
placeholder="Código de reserva"
required
/>

<button type="submit">
Cancelar reserva
</button>

</form>

<p v-if="message" class="success">
{{ message }}
</p>

<p v-if="errorMessage" class="error">
{{ errorMessage }}
</p>

</div>

</template>

<script>

import api from "../services/api"

export default{

data(){

return{

reservationCode:"",
message:"",
errorMessage:""

}

},

methods:{

async cancelReservation(){

this.message=""
this.errorMessage=""

try{

await api.post("/reservations/cancel/",{

reservation_code:this.reservationCode

})

this.message="Reserva cancelada correctamente."

}catch(error){

this.errorMessage=
error.response?.data?.error ||
"Error al cancelar la reserva."

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
max-width:400px;
margin:auto;
}

input{
width:100%;
margin-bottom:12px;
padding:10px;
border:1px solid #ccc;
border-radius:8px;
}

button{
padding:10px 16px;
border:none;
border-radius:8px;
background:#dc2626;
color:white;
cursor:pointer;
}

.error{
color:red;
margin-top:10px;
}

.success{
color:green;
margin-top:10px;
}

</style>