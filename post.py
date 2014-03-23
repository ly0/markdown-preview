#coding=utf-8
import sys
import markdown2
import re

template = '''
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <style>
/*

Handwritten by Michiel de Graaf.

*/

@import url(http://fonts.googleapis.com/css?family=PT+Serif:400,700,400italic,700italic);
@import url(http://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700,400italic,700italic);
@import url(http://fonts.googleapis.com/css?family=Source+Code+Pro:400,700);

article, aside, details, figcaption, figure, footer, header, hgroup, menu, nav, section, dialog{
  display: block;
}
*{
  margin: 0;
  padding: 0;
}

/* Basics
 *************************************/

body{
  font-family: "PT Serif", Georgia, Times, "Times New Roman", "WenQuanYi Micro Hei", serif;
  font-size: 95%;
  line-height: 1.6;
  vertical-align: baseline;
  color: #18191a;
  background: #fff;
  -webkit-font-smoothing: antialiased;
}
a{
  cursor: pointer;
  color: rgb(184,23,35);
  text-decoration: none;
  transition: all .25s;
}
a:hover{
  border-bottom: 1px solid rgba(184,23,35,0.5);
}
h1,h2,h3,h4{
  font-family: "Source Sans Pro", Futura, "Helvetica Neue", Helvetica, "Lantinghei SC", "Kaiti SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
	line-height: 1.2;
}
h1 a, h2 a, h3 a, h4 a{
	color: #000;
}
h1 a:hover, h2 a:hover, h3 a:hover, h4 a:hover{
	border-bottom: none;
}
p.meta{
	color: rgb(164,171,178);
}
p.meta a{
  color: rgb(164,171,178);
}
p.meta a:hover{
  border-bottom: 1px solid rgba(164,171,178,0.5);
}
code{
  font-family: Menlo, Monaco, Consolas, "Source Code Pro", monospace;
}
.container{
  overflow: hidden;
  width: 800px;
  margin: 0 auto;
}

dl{
	margin: 1em 0;
}
dd{
	margin-left: 40px;
}

/* Articles
 *************************************/

section[role="main"]{
  overflow: visible;
  padding-top: 20px;
  padding-bottom: 80px;
}
article{
  margin-top: 60px;
}
article header{
  overflow: hidden;
  margin-bottom: 16px;
}
article header h1{
  font-size: 2.0em;
}
article header p.meta{
  font-family: "Open Sans", Futura, "Helvetica Neue", Helvetica, "Lantinghei SC", "Kaiti SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
	font-size: .75em;
	font-weight: 500;
	letter-spacing: .2em;
	margin-bottom: 8px;
}
article header time{
  text-transform: uppercase;
}

article p#tags{
	float: left;
}
article .content{
  font-size: 1.25em;
}
article .content h1{
  font-size: 2.5em;
  margin: 45px 0 30px
}
article .content h2{
  font-size: 2em;
  margin: 45px 0 30px
}
article .content h3{
  font-size: 1.7em;
  margin: 40px 0 30px;
}
article .content h4{
  font-size: 1.4em;
  margin: 35px 0 20px;
}
article .content h5{
  font-size: 1.2em;
  margin: 30px 0 20px;
}
article .content h6{
  font-size: 1.0em;
  margin: 30px 0 20px;
}
article .content p{
  margin-top: 20px;
  margin-bottom: 20px;
}
article .content img,
article .content video{
  display: block;
/*  min-width: 50%;*/
  max-width: 100%;
  height: auto;
  margin: auto;
  padding: 10px 0;
}
article .content img.inline{
	display: inline;
}
article .content ul,
article .content ol{
  margin: 0 0 20px 40px;
}
article .content p code{
  font-size: .85em;
	overflow-wrap: break-word;
	word-wrap: break-word;;
}
article .content .intro{
  margin-top: 0;
}
article .content blockquote{
	  font-family: "PT Serif", Georgia, Times, "Times New Roman", "STFangsong", serif;
	  padding-left: 10px;
	  border-left: 2px solid #ccc;
}



/* Code
 *************************************/
div.code {
  font-size: .85em;
	margin-bottom: 20px;
	padding: 10px;
	overflow: auto;
	border-radius: 4px;
	border: 1px solid hsl(0,0%,84%);
	box-shadow: 0 1px 1px hsla(0,0%,0%,.05),;
	background-color: hsla(0,0%,0%,.02);
 }
code .hll { background-color: #ffffcc }
code  { color: #586e75 }
code .code-c { color: #93a1a1; font-style: italic } /* Comment */
code .code-g { color: #d33682 } /* Generic */
code .code-k { color: #859900 } /* Keyword */
code .code-l { color: #2aa198 } /* Literal */
code .code-n { color: #268bd2 } /* Name */
code .code-cm { color: #93a1a1; font-style: italic } /* Comment.Multiline */
code .code-cp { color: #93a1a1; font-style: italic } /* Comment.Preproc */
code .code-c1 { color: #93a1a1; font-style: italic } /* Comment.Single */
code .code-cs { color: #93a1a1; font-style: italic } /* Comment.Special */
code .code-gd { color: #d33682 } /* Generic.Deleted */
code .code-ge { color: #d33682 } /* Generic.Emph */
code .code-gr { color: #d33682 } /* Generic.Error */
code .code-gh { color: #d33682 } /* Generic.Heading */
code .code-gi { color: #d33682 } /* Generic.Inserted */
code .code-go { color: #d33682 } /* Generic.Output */
code .code-gp { color: #d33682 } /* Generic.Prompt */
code .code-gs { color: #d33682 } /* Generic.Strong */
code .code-gu { color: #d33682 } /* Generic.Subheading */
code .code-gt { color: #d33682 } /* Generic.Traceback */
code .code-kc { color: #859900; font-weight: bold } /* Keyword.Constant */
code .code-kd { color: #859900 } /* Keyword.Declaration */
code .code-kn { color: #dc322f; font-weight: bold } /* Keyword.Namespace */
code .code-kp { color: #859900 } /* Keyword.Pseudo */
code .code-kr { color: #859900 } /* Keyword.Reserved */
code .code-kt { color: #859900; font-weight: bold } /* Keyword.Type */
code .code-ld { color: #2aa198 } /* Literal.Date */
code .code-m { color: #2aa198; font-weight: bold } /* Literal.Number */
code .code-s { color: #2aa198 } /* Literal.String */
code .code-na { color: #268bd2 } /* Name.Attribute */
code .code-nb { color: #cb4b16 } /* Name.Builtin */
code .code-nc { color: #cb4b16 } /* Name.Class */
code .code-no { color: #268bd2 } /* Name.Constant */
code .code-nd { color: #268bd2 } /* Name.Decorator */
code .code-ni { color: #268bd2 } /* Name.Entity */
code .code-ne { color: #268bd2 } /* Name.Exception */
code .code-nf { color: #268bd2 } /* Name.Function */
code .code-nl { color: #268bd2 } /* Name.Label */
code .code-nn { color: #268bd2 } /* Name.Namespace */
code .code-nx { color: #268bd2 } /* Name.Other */
code .code-py { color: #268bd2 } /* Name.Property */
code .code-nt { color: #268bd2; font-weight: bold } /* Name.Tag */
code .code-nv { color: #268bd2 } /* Name.Variable */
code .code-ow { color: #859900 } /* Operator.Word */
code .code-w { color: #586e75 } /* Text.Whitespace */
code .code-mf { color: #2aa198; font-weight: bold } /* Literal.Number.Float */
code .code-mh { color: #2aa198; font-weight: bold } /* Literal.Number.Hex */
code .code-mi { color: #2aa198; font-weight: bold } /* Literal.Number.Integer */
code .code-mo { color: #2aa198; font-weight: bold } /* Literal.Number.Oct */
code .code-sb { color: #2aa198 } /* Literal.String.Backtick */
code .code-sc { color: #2aa198 } /* Literal.String.Char */
code .code-sd { color: #2aa198 } /* Literal.String.Doc */
code .code-s2 { color: #2aa198 } /* Literal.String.Double */
code .code-se { color: #2aa198 } /* Literal.String.Escape */
code .code-sh { color: #2aa198 } /* Literal.String.Heredoc */
code .code-si { color: #2aa198 } /* Literal.String.Interpol */
code .code-sx { color: #2aa198 } /* Literal.String.Other */
code .code-sr { color: #2aa198 } /* Literal.String.Regex */
code .code-s1 { color: #2aa198 } /* Literal.String.Single */
code .code-ss { color: #2aa198 } /* Literal.String.Symbol */
code .code-bp { color: #cb4b16 } /* Name.Builtin.Pseudo */
code .code-vc { color: #268bd2 } /* Name.Variable.Class */
code .code-vg { color: #268bd2 } /* Name.Variable.Global */
code .code-vi { color: #268bd2 } /* Name.Variable.Instance */
code .code-il { color: #2aa198; font-weight: bold } /* Literal.Number.Integer.Long */

/* Responsiveness
 *************************************/

@media screen and (max-width: 720px){
	body{
	  font-size: 90%;
	}
  .container{
    width: 85%;
  }
}

  </style>
</head>
<body>
  <section role="main" class="container">
	  <article>
	    <section class="content">
	      {{content}}
	    </section>
	  </article>  
  </section>
    
</body>
</html>

'''

text = sys.stdin.read()
markdown = markdown2.markdown(text)
print template.replace('{{content}}',markdown).encode('utf-8')

