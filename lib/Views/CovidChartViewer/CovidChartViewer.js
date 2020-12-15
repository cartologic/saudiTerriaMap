import React, { useState, useEffect } from "react";
import Proptypes from "prop-types";
import Plotly from "plotly.js";
import MenuPanel from "terriajs/lib/ReactViews/StandardUserInterface/customizable/MenuPanel";
import PanelStyles from "terriajs/lib/ReactViews/Map/Panels/panel.scss";
import classNames from "classnames";
import Loader from "react-loader-spinner";
import Styles from "../related-maps.scss";
import CovidChart from "./CovidChart/CovidChart";

const CovidChartViewer = props => {
  const [regionsData, setRegionsData] = useState([]);
  const [governoratesData, setGovernoratesData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const regionsURL =
      "http://mapsaudi.com/geoserver/ows?outputFormat=csv&service=WFS&srs=EPSG%3A3857&request=GetFeature&typename=geonode%3Ar&version=1.0.0";
    const governoratesURL =
      "http://mapsaudi.com/geoserver/ows?outputFormat=csv&service=WFS&srs=EPSG%3A3857&request=GetFeature&typename=geonode%3Asagov&version=1.0.0";

    Plotly.d3.csv(regionsURL, data => {
      setRegionsData(data);
    });
    Plotly.d3.csv(governoratesURL, data => {
      setGovernoratesData(data);
    });

    if (regionsData.length !== 0 && governoratesData.length !== 0) {
      setLoading(false);
    }
  }, [regionsData.length, governoratesData.length]);

  const dropdownTheme = {
    inner: Styles.dropdownInner,
    icon: "lineChart"
  };

  const dataType = {
    regions: "Regions",
    governorates: "Governorates"
  };

  return (
    <MenuPanel
      theme={dropdownTheme}
      btnText="Saudi COVID-19 Statistics"
      smallScreen={props.smallScreen}
      viewState={props.viewState}
      btnTitle="See Saudi COVID-19 charts"
    >
      <div className={classNames(PanelStyles.header)}>
        <label className={PanelStyles.heading}>Saudi COVID-19 Statistics</label>
      </div>
      <p>
        This graph visualize some statistics about COVID-19 cases in Saudi
        Arabia.
      </p>
      <div className={classNames(PanelStyles.section, Styles.section)}>
        {!loading ? (
          <>
            <CovidChart data={regionsData} dataType={dataType.regions} />
            <CovidChart
              data={governoratesData}
              dataType={dataType.governorates}
            />
          </>
        ) : (
          <Loader type="Oval" color="#4BAE53" height={100} width={100} />
        )}
      </div>
    </MenuPanel>
  );
};

CovidChartViewer.propTypes = {
  viewState: Proptypes.object.isRequired,
  smallScreen: Proptypes.bool
};

export default CovidChartViewer;
