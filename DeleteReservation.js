
import React from 'react';


class DeleteReservation extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            rezervationName: '',
            officeName: '',
            startDate: '',
            endDate: '',
        }
    }

    const DeleteReservation = () => {
        return(
            <h1>DeleteReservation</h1>
            <div  >
                <div>  
                    <form className='reservation-form' >
                    <TextField required id="standard-required" label="Rezarvasyon Sil" />
                    <TextField
                    
                        label="Next appointment"
                        type="datetime-local"
                        defaultValue={Date()}
                        InputLabelProps={{
                            shrink: false,
                        }}
                    />
                </form>
                    
                </div>
            </div>
                )
    }
}


export default DeleteReservation;