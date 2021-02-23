import logo from './logo.svg';
import Navbar from "./components/Navigation/Navbar";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

function App() {

  return (
    <div className="App">

        <Router>    {/*для работы <Link>*/}
            <Navbar />    {/*вызов нав бара*/}
        </Router>

    </div>
  );
}

export default App;
