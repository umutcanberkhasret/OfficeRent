import React from 'react';
import InputLabel from '@material-ui/core/InputLabel';
import Input from '@material-ui/core/Input';
import Button from '@material-ui/core/Button';
import ReservationService from '../../services/ReservationService';


export default class AddReservation extends React.Component {
  constructor(props){
      super(props);
    //   this.reservationService = new ReservationService();
      this.state = {
        officeName: "",
        date: "",
        errors: {
          officeName: false,
          date: false
        }
      }
  }

  handleChange = (key, value) => {
    const stateObj = {
      [key]: value,
      errors: {...this.state.errors}
    }
    // if the user input is not as we wanted, we push an error and input boxes wont let the user to submit data
    if(value) {
      stateObj.errors[key] = false
    }
    else {
      stateObj.errors[key] = true
    }

    this.setState(stateObj)
  };

  handleSubmit = (event) => {
    event.preventDefault()

    const errors = {}
    if(!this.state.officeName){
        errors.officeName = true
    }

    // checks whether the given date is prior to current date
    if(!this.state.date || new Date(this.state.date) < new Date()) {
        errors.date = true
    }
    
    // tracks the number of errors and sets them within the state
    if(Object.keys(errors).length > 0) {
      return this.setState({
        errors: errors
      })
    }
    
    // we are creating the reservation object that is intended to be sent out to the endpoint. The formed object will be passed through Axios
    const reservationObject = {
      officeName: this.state.officeName,
      date: this.state.date
    }

    console.log(reservationObject);
    // service call inbound, once we upload the endpoint we are going to be able to write to the db
    // reservationService.add(reservationObject)

    this.setState({
      officeName: "",
      date: ""
    })
  }
  
  render(){
  return (
    <div>
      <form onSubmit={this.handleSubmit}>
        <InputLabel error={this.state.errors.officeName} value={this.state.officeName}>Ofis Adı</InputLabel>
        <Input error={this.state.errors.officeName} value={this.state.officeName} onChange={(e) => this.handleChange("officeName", e.target.value)}/>

        <InputLabel error={this.state.errors.date} value={this.state.date}>Tarih</InputLabel>
        <Input error={this.state.errors.date} value={this.state.date} type="date" onChange={(e) => this.handleChange("date", e.target.value)}/>

    
        <Button variant="contained" size="medium" color="primary" type="submit" >
        Rezervasyon Ekle
        </Button>
      </form>
        
    </div>
  );
  }
}