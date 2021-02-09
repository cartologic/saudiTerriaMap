import {
  Menu,
  Nav
} from "terriajs/lib/ReactViews/StandardUserInterface/customizable/Groups";
import MeasureTool from "terriajs/lib/ReactViews/Map/Navigation/MeasureTool";
import MenuItem from "terriajs/lib/ReactViews/StandardUserInterface/customizable/MenuItem";
import PropTypes from "prop-types";
import React from "react";
import StandardUserInterface from "terriajs/lib/ReactViews/StandardUserInterface/StandardUserInterface.jsx";
import version from "../../version";
import CovidChartViewer from "./CovidChartViewer/CovidChartViewer";
import ToggleLanguage from "./ToggleLanguage";

import "./global.scss";
import "../Models/i18n";

export default function UserInterface(props) {
  return (
    <StandardUserInterface {...props} version={version}>
      <Menu>
        <CovidChartViewer viewState={props.viewState} />
        <MenuItem caption="About" href="about.html" key="about-link" />
      </Menu>
      <Menu>
        <ToggleLanguage />
      </Menu>
      <Nav>
        <MeasureTool terria={props.viewState.terria} key="measure-tool" />
      </Nav>
    </StandardUserInterface>
  );
}

UserInterface.propTypes = {
  terria: PropTypes.object,
  viewState: PropTypes.object
};
