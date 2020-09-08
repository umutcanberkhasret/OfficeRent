import React from 'react';
import TextField from '@material-ui/core/TextField';
import './addreservation.css'

class AddReservation extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            rezervationName: '',
            officeName: '',
            startDate: '',
            endDate: '',
        }
    }

    render() {
        return (
            <div  >
                <div>  
                    <form className='reservation-form' >
                    <TextField required id="standard-required" label="Rezarvasyon Alıcı" />
                    <TextField
                        id="datetime-local"
                        label="Next appointment"
                        type="datetime-local"
                        defaultValue={Date()}
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                </form>
                    
                </div>
            </div>
        )
    }
}


export default AddReservation;