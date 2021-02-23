import logo from './logo.svg';
import Navbar from "./components/Navigation/Navbar";
import CategoryDetail from "./components/Category/CategoryDetail";
import PostDetail from "./components/Posts/PostDetail";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

function App() {

  return (
    <div className="App">

        <Router>    {/*для работы <Link>*/}
            <Navbar />    {/*вызов нав бара*/}
            <Switch>
                <Route path="/posts/:id" exact component={PostDetail} />
                <Route path="/category/:id" exact component={CategoryDetail} />
            </Switch>

        </Router>

    </div>
  );
}

export default App;
