import { useEffect, useState } from "react"

function Dashboard(){

const [events,setEvents] = useState([])

useEffect(()=>{

const ws = new WebSocket("ws://localhost:8000/ws")

ws.onmessage = (event)=>{

const data = JSON.parse(event.data)

setEvents(prev=>[data,...prev])

}

},[])

return(

<div>

<h1>SentimPay Ultra Dashboard</h1>

{events.map((e,i)=>(

<div key={i}>

<p>Sentiment: {e.sentiment}</p>
<p>Transaction: {e.transaction}</p>

</div>

))}

</div>

)

}

export default Dashboard