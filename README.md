SimpleTelemetryProvider
=============

Simple JSON-RPC 2.0 compilant telemetry provider for [UE4]s UBT (Unreal Build Tool). The provider just sends UBT events to a hosted JSON-RPC 2.0 web service to be processed further.

Usage
----

To use the provider just copy the folder containing the source (SimpleTelemetryProvider) into the UnreadBuildTool in your visual Studio Solution. For Linux and Mac add the folder into the required project files.

Once you have the folder setup you only have to change the URL and the method name (depending on your WebServer)

```C#
class SimpleTelemetryProvider : Telemetry.IProvider
{
    [...]
    
    private string HostUrl = "http://<you/host/>:8080/api";
    private static string MethodName = "UBT";
    
    [...]
}
```

A simple JSON RPC 2.0 python server has been provided to be able to start getting your stats up and running as fast as possible. Just use the ```run.[bat|sh]``` to launch the server. The server will run by default on port 8080, check the launch script to specifiy a different port. 

The server requires a set of prerequisite:
* Python 2.7
* Web.Py
* Setuptools
* PyMongo

To configure your mongo db connection just change the connection URL which can be found in ```ubt.config.py```


License
----

The MIT License (MIT)

Copyright (c) 2014 Moritz Wundke

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Legal info
----

Unreal® is a trademark or registered trademark of Epic Games, Inc. in the United States of America and elsewhere.

Unreal® Engine, Copyright 1998 – 2014, Epic Games, Inc. All rights reserved.

[UE4]:https://www.unrealengine.com/
