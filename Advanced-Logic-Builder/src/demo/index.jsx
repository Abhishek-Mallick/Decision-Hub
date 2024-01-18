/*eslint no-unused-vars: ["off", {"varsIgnorePattern": "^_"}]*/
import React, {Component} from "react";
import {
  Utils, Query, Builder
} from "@react-awesome-query-builder/ui";
import loadedConfig from "./config";
import loadedInitValue from "./init_value";
import loadedInitLogic from "./init_logic";
import { CopyToClipboard } from 'react-copy-to-clipboard';

const stringify = JSON.stringify;
const {jsonLogicFormat, queryString, mongodbFormat, sqlFormat, getTree, checkTree, loadTree, uuid, loadFromJsonLogic} = Utils;
const preStyle = { backgroundColor: "#74c69d", margin: "10px", padding: "10px" };
const preErrorStyle = { backgroundColor: "lightpink", margin: "10px", padding: "10px" };

const emptyInitValue = {"id": uuid(), "type": "group"};

// get init value in JsonTree format:
const initValue = loadedInitValue && Object.keys(loadedInitValue).length > 0 ? loadedInitValue : emptyInitValue;
const initTree = checkTree(loadTree(initValue), loadedConfig);

export default class DemoQueryBuilder extends Component {
    
  state = {
    tree: initTree,
    config: loadedConfig
  };

  render = () => (
    <div>
      <Query 
        {...loadedConfig} 
        value={this.state.tree}
        onChange={this.onChange}
        renderBuilder={this.renderBuilder}
      />

      <button onClick={this.resetValue}>reset</button>
      <button onClick={this.clearValue}>clear</button>

      <div className="query-builder-result">
        {this.renderResult(this.state)}
      </div>
    </div>
  );

  resetValue = () => {
    this.setState({
      tree: initTree, 
    });
  };

  clearValue = () => {
    this.setState({
      tree: loadTree(emptyInitValue), 
    });
  };

  renderBuilder = (props) => (
    <div className="query-builder-container" style={{padding: "10px"}}>
      <div className="query-builder">
        <Builder {...props} />
      </div>
    </div>
  );
    
  onChange = (immutableTree, config) => {
    this.immutableTree = immutableTree;
    this.config = config;
    this.updateResult();

    // `jsonTree` or `logic` can be saved to backend
    // (and then loaded with `loadTree` or `loadFromJsonLogic` as seen above)
    const jsonTree = getTree(immutableTree);
    const {logic, data, errors} = jsonLogicFormat(immutableTree, config);
  };

  updateResult = () => {
    this.setState({tree: this.immutableTree, config: this.config});
  };

  renderResult = ({tree: immutableTree, config}) => {
    const {logic, data, errors} = jsonLogicFormat(immutableTree, config);
    const sqlValue = stringify(sqlFormat(immutableTree, config), undefined, 2);

    return (
      <div>
        <br />
        <hr/>
        <div>
          sqlFormat:
          <pre style={preStyle}>
            {sqlValue}
          </pre>
          
          <CopyToClipboard text={sqlValue} onCopy={() => this.setState({ copied: true })}>
            <button>Copy SQL query</button>
          </CopyToClipboard>

          {this.state.copied && <span style={{ color: 'red', marginLeft: '10px' }}>Copied.</span>}
        </div>
        <hr/>
        <div>
  jsonLogicFormat:
  {errors.length > 0 &&
    <pre style={preErrorStyle}>
      {stringify(errors, undefined, 2)}
    </pre>
  }
  {!!logic &&
    <pre style={preStyle}>
      {"// Rule"}:<br />
      {stringify(logic, undefined, 2)}
      <br />
      <hr />
      {"// Data"}:<br />
      {stringify(data, undefined, 2)}
    </pre>
  }

  <CopyToClipboard text={JSON.stringify(logic, undefined, 2)} onCopy={() => this.setState({ copiedRule: true })}>
    <button style={{ marginRight: '10px' }}>Copy Rule</button>
  </CopyToClipboard>

  {this.state.copiedRule && <span style={{ color: 'red', marginLeft: '10px' }}>Copied Rule.</span>}

  <CopyToClipboard text={JSON.stringify(data, undefined, 2)} onCopy={() => this.setState({ copiedData: true })}>
    <button style={{ marginRight: '10px' }}>Copy Data</button>
  </CopyToClipboard>

  {this.state.copiedData && <span style={{ color: 'red', marginLeft: '10px' }}>Copied Data.</span>}
</div>
<hr />
<div>
          Tree: 
          <pre style={preStyle}>
            {stringify(getTree(immutableTree), undefined, 2)}
          </pre>
        </div>

      </div>
    );
  };

}
