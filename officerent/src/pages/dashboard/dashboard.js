import React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import Button from '@material-ui/core/Button';
import TableCell from '@material-ui/core/TableCell';
import TableRow from '@material-ui/core/TableRow';
import { NavLink } from 'react-router-dom';
import Styles from './dashboard.module.css';


class Dashboard extends React.Component {
    constructor(props){
        super(props);
        this.state = {
          data: [
            {id: 1, officeName: "Office 1", date: new Date("2020/12/11")},
            {id: 2, officeName: "Office 2", date: new Date("2020/12/24")},
            {id: 3, officeName: "Pffoce 3", date: new Date("2020/12/27")},
            {id: 4, officeName: "Office 4", date: new Date("2021/1/11")}
          ]
        }
    }
    
    componentDidMount() {
        /*
        try{
          reservationService.get()
          // todo do date formatting
        }
        catch(error){
          // todo handle error
        }
        */
    }
    
    handleDelete = async (index) => {
        const data = [...this.state.data];
    
        try {
          // await reservationService.delete(data.id)
    
          data.splice(index, 1);
    
          this.setState({
            data: data
          })
        }
        catch(error) {
          // todo error handling
        }
        
      }
    
    render() {
        return (
            <div className={Styles.layout}>
                <div>
                    {/* the table that is consisting of the added reservations will be presented below */}
                    <div>
                        <Table>
                            <TableBody>
                                {this.state.data.map((reservation, index) => (
                                    <TableRow key={reservation.id}>
                                        <TableCell component="th" scope="row">
                                            {reservation.officeName}
                                        </TableCell>
                                        <TableCell component="th" scope="row">
                                            {reservation.date.getFullYear() + "/" + (reservation.date.getMonth() + 1) + "/" + reservation.date.getDate()}
                                        </TableCell>
                                        <TableCell align="right"><Button onClick={this.handleDelete}>Sil</Button></TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </div>
                </div>
                <div className={Styles.buttons}>
                    <NavLink style={{ textDecoration: 'none' }} to="/addreservation">
                        <Button variant="contained" size="medium" color="primary" >
                            Rezervasyon Ekle
                        </Button>
                    </NavLink>

                    <NavLink style={{ textDecoration: 'none' }} to="/deletereservation">
                        <Button variant="contained" size="medium" color="primary" >
                            Rezervasyon Sil
                        </Button>
                    </NavLink>
                </div>
            </div>
        )
    }
}

export default Dashboard;