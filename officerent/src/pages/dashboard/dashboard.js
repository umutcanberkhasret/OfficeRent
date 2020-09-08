import React from 'react';
import Styles from './dashboard.module.css';
import Button from '@material-ui/core/Button';
import {NavLink} from 'react-router-dom';


class Dashboard extends React.Component {
    render() {
        return (
            <div className={Styles.layout}>
                <div>
                    <h1>takvim</h1>
                </div>
                <div className={Styles.buttons}>
                    <NavLink style={{ textDecoration: 'none' }} to="/addreservation">
                        <Button variant="contained" size="medium" color="primary" >
                            Add Reservation
                        </Button>
                    </NavLink>

                    <NavLink style={{ textDecoration: 'none' }} to="/deletereservation">
                        <Button variant="contained" size="medium" color="primary" >
                            Delete Reservation
                        </Button>
                    </NavLink>
                </div>
            </div>
        )
    }
}

export default Dashboard;