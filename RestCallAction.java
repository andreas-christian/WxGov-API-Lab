package com.ibm.openpages.ext.custom.workflow.action;

import java.util.List;
import com.ibm.openpages.api.resource.IGRCObject;
import com.ibm.openpages.api.workflow.actions.AbstractCustomAction;
import com.ibm.openpages.api.workflow.actions.IWFCustomProperty;
import com.ibm.openpages.api.workflow.actions.IWFOperationContext;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;

public class RestCallAction extends AbstractCustomAction {

    public RestCallAction(IWFOperationContext arg0, List<IWFCustomProperty> arg1) {
        super(arg0, arg1);
    }

    protected void process() throws Exception {
        IWFOperationContext context = this.getContext();
        IGRCObject grcObject = context.getResource();
        String grcObjectId = grcObject.getId().toString();

        System.out.println("****** RestCallAction is executed... ***********");

        // the following properties must be specified in the custom workflow action 
	// to be able successfully execute the REST call
        String ip_address = this.getPropertyValue("ip_address");
        String endpoint = this.getPropertyValue("endpoint");
        String username = this.getPropertyValue("username");
	String url_str = "http://"+ip_address+":8080"+endpoint+"?id="+grcObjectId;

	if ( ip_address == null) {
		System.out.println("Property <ip_address> must be specified in the workflow action!");
		return;
	}
	if ( endpoint == null) {
		System.out.println("Property <endpoint> must be specified in the workflow action!");
		return;
	}
	if ( username == null) {
		System.out.println("Property <username> must be specified in the workflow action!");
		return;
	}

        System.out.println("****** RestCallAction parameters:");

        System.out.println("ip_address=" + ip_address);
        System.out.println("endpoint=" + endpoint);
        System.out.println("username=" + username);
        System.out.println("grcObjectId=" + grcObjectId);
        System.out.println("url_str=" + url_str);

        URL urlForGetRequest = new URL( url_str);
        String readLine = null;
        HttpURLConnection connection = (HttpURLConnection) urlForGetRequest.openConnection();
        connection.setRequestMethod( "GET");
        connection.setRequestProperty( "username", username);
        int responseCode = connection.getResponseCode();
	System.out.println( "ResponseCode: "+responseCode);

        if (responseCode == HttpURLConnection.HTTP_OK) {
            System.out.println("******RestCallAction successfully executed!");
            BufferedReader in = new BufferedReader(
                new InputStreamReader(connection.getInputStream()));
            StringBuffer response = new StringBuffer();
            while ((readLine = in .readLine()) != null) {
                response.append(readLine);
            } in .close();
            // print result
            System.out.println( "JSON String Result: ");
            System.out.println( response.toString());
        }
    }

}
