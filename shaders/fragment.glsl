#version 330
#define PI 3.14159265
in vec2 TexCoord;

uniform vec4 SkyColor = vec4( 0.3, 0.3, 0.9, 1.0 );
uniform vec4 CloudColor = vec4( 1.0, 1.0, 1.0, 1.0 );

uniform sampler2D NoiseTex;

layout ( location = 0 ) out vec4 FragColor;

void main()
{
    vec4 matrix = texture(NoiseTex, TexCoord);
    float t = (cos( matrix.g * PI ) + 1.0) / 2.0;
    vec4 color = mix( SkyColor, CloudColor, t );
    FragColor = vec4( color.rgb , 1.0 );
}