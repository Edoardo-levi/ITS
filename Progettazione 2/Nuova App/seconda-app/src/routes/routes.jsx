import About from "./About";
import ErrorPage from "./ErrorPage";
import Home from "./Home";
import MyProfile from "./MyProfile";
import Profiles from "./Profiles";
import SingleProfile from "./SingleProfile";

export const routes = [
  {
    path: "/",
    element: <Home></Home>,
  },
  {
    path: "/about",
    element: <About></About>,
  },
  {
    path: "/profiles/",
    element: <Profiles></Profiles>,
    children: [
      {
        path: ":id",
        element: <SingleProfile></SingleProfile>,
      },
      {
        path: "me",
        element: <MyProfile></MyProfile>,
      },
    ],
  },
  {
    path: "*",
    element: <ErrorPage></ErrorPage>,
  },
];