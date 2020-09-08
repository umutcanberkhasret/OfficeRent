import React from 'react';
import './App.css';
import { Route, Switch, Redirect } from 'react-router-dom';
import Dashboard from './pages/dashboard/dashboard';
import AddReservation from './pages/addreservation/add-reservation';
import DeleteReservation from './pages/deletereservation/delete-reservation';
import Header from './components/header/Header'

function App() {
  return (
    <div className="App">
      <Header />
      <Switch>
        <Route exact strict path='/dashboard' component={Dashboard} />
        <Route exact strict path='/addreservation' component={AddReservation} />
        <Route exact strict path='/deletereservation' component={DeleteReservation} />
        <Redirect to='/dashboard' />
      </Switch>
    </div>
  );
}

export default App;
