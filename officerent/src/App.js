import React from 'react';
import './App.css';
import { Route, Switch, Redirect } from 'react-router-dom';

import Dashboard from './pages/dashboard';
import AddReservation from './pages/add-reservation';
import DeleteReservation from './pages/delete-reservation';

function App() {
  return (
    <div className="App">
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
