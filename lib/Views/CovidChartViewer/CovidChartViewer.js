import React, { useState, useEffect } from "react";
import Proptypes from "prop-types";
import Plotly from "plotly.js";
import MenuPanel from "terriajs/lib/ReactViews/StandardUserInterface/customizable/MenuPanel";
import PanelStyles from "terriajs/lib/ReactViews/Map/Panels/panel.scss";
import classNames from "classnames";
import Loader from "react-loader-spinner";
import { useTranslation } from "react-i18next";
import Styles from "../related-maps.scss";
import CovidChart from "./CovidChart/CovidChart";

const CovidChartViewer = props => {
  const [regionsData, setRegionsData] = useState([]);
  const [governoratesData, setGovernoratesData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const regionsURL =
      "https://mapsaudi.com/geoserver/ows?outputFormat=csv&service=WFS&srs=EPSG%3A3857&request=GetFeature&typename=geonode%3Ar&version=1.0.0";
    const governoratesURL =
      "https://mapsaudi.com/geoserver/ows?outputFormat=csv&service=WFS&srs=EPSG%3A3857&request=GetFeature&typename=geonode%3Asagov&version=1.0.0";

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

  const { t } = useTranslation();

  return (
    <MenuPanel
      theme={dropdownTheme}
      btnText={t("covid19-charts.saudi-covid-statistics")}
      smallScreen={props.smallScreen}
      viewState={props.viewState}
      btnTitle={t("covid19-charts.saudi-covid-charts")}
    >
      <div className={classNames(PanelStyles.header)}>
        <label className={PanelStyles.heading}>
          {t("covid19-charts.saudi-covid-statistics")}
        </label>
      </div>
      <p>{t("covid19-charts.saudi-covid-description")}</p>
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
