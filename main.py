# !!! v Change This v !!!
creator = "blitzgoodszz"
projectName = "quiz-program"
projectNameWithoutDash = "quizprogram"
userTableName = "User"
modelName = "UserRole"
createdBy = False
createdDate = False
lastModifiedBy = False
lastModifiedDate = False
path = "../" + projectName +"/src/main/java/com/" + creator + "/" + projectNameWithoutDash
modelAttr = [
    {"name": "roleName", "dataType": "String"},
]
# modelAttr = [
#     {"name": "username", "dataType": "String"},
#     {"name": "password", "dataType": "String"},
#     {"name": "email", "dataType": "String"},
#     {"name": "name", "dataType": "String"},
#     {"name": "gender", "dataType": "String"},
#     {"name": "phone", "dataType": "String"},
#     {"name": "address", "dataType": "String"},
#     {"name": "dob", "dataType": "Date"},
#     {"name": "profilePicture", "dataType": "String"}
# ]
# !!! ^ Change This ^ !!!

import os
dirList = ["model", "controller", "repository", "service"]
for d in dirList:
    if os.path.exists(path + "/" + d) is False: os.makedirs(path + "/" + d)

def getAudit():
    audit = ""
    if createdBy: audit += ("\t@CreatedBy" + "\n" + "\tprivate User createdBy;" + "\n")
    if createdDate: audit += ("\t@CreatedDate" + "\n" + "\tprivate Date createdDate;" + "\n")
    if lastModifiedBy: audit += ("\t@LastModifiedBy" + "\n" + "\tprivate User lastModifiedBy;" + "\n")
    if lastModifiedDate: audit += ("\t@LastModifiedDate" + "\n" + "\tprivate Date lastModifiedDate;" + "\n")
    return audit

def getAuditImport():
    auditImport = ""
    if createdBy: auditImport += ("import org.springframework.data.annotation.CreatedBy;" + "\n")
    if createdDate: auditImport += ("import org.springframework.data.annotation.CreatedDate;" + "\n")
    if lastModifiedBy: auditImport += ("import org.springframework.data.annotation.LastModifiedBy;" + "\n")
    if lastModifiedDate: auditImport += ("import org.springframework.data.annotation.LastModifiedDate;" + "\n")
    return auditImport

def getAuditGetterSetter():
    auditGetterSetter = ""
    if createdBy: auditGetterSetter += ("\n\tpublic User getCreatedBy() { return createdBy; }" + "\n")
    if createdDate: auditGetterSetter += ("\n\tpublic Date getCreatedDate() { return createdDate; }" + "\n")
    if lastModifiedBy: auditGetterSetter += ("\n\tpublic User getCreatedBy() { return lastModifiedBy; }" + "\n")
    if lastModifiedDate: auditGetterSetter += ("\n\tpublic Date getCreatedBy() { return lastModifiedDate; }" + "\n")
    return auditGetterSetter

with open(path + "/model/" + modelName + ".java", "w") as model:
    attr = ""
    audit = getAudit()
    auditImport = getAuditImport()
    extraImport = ""
    extraImportChecker = [0] # Date
    getterSetter = ""

    for a in modelAttr:
        attr += ("\tprivate " + a["dataType"] + " " + a["name"] + ";") + "\n"
        upperName = a["name"].upper()[0] +  a["name"][1:]
        getterSetter += ("\n\tpublic " + a["dataType"] + " get" + upperName + "() { return " + a["name"] + "; }") + "\n"
        getterSetter += ("\n\tpublic void set" + upperName + "(" + a["dataType"] + " " + a["name"] + ") { this." + a["name"] + " = " + a["name"] + "; }") + "\n"
        if a["dataType"] == "Date" and extraImportChecker[0] == 0:
            extraImport += "import java.util.Date;" + "\n"
            extraImportChecker[0] = 1
        if createdDate and extraImportChecker[0] == 0:
            extraImport += "import java.util.Date;" + "\n"
            extraImportChecker[0] = 1
    
    getterSetter += getAuditGetterSetter()

    model.write(
        "package com." + creator + "." + projectNameWithoutDash + ".model;" + "\n" +
        "\n" +
        auditImport + "\n" +
        "import javax.persistence.Entity;" + "\n" +
        "import javax.persistence.GeneratedValue;" + "\n" +
        "import javax.persistence.GenerationType;" + "\n" +
        "import javax.persistence.Id;" + "\n" +
        extraImport + "\n" +
        "@Entity" + "\n" +
        "public class " + modelName + " {" + "\n" +
        "\t@Id" + "\n" +
        "\t@GeneratedValue(strategy = GenerationType.IDENTITY)" + "\n" +
        "\tprivate int id;" + "\n" +
        attr + "\n" +
        audit + "\n" +
        "\tpublic " + modelName + "() {}" + "\n" +
        getterSetter + "\n" +
        "}" + "\n" 
    )

with open(path + "/controller/" + modelName + "Controller.java", "w") as controller:
    controller.write(
        "package com." + creator + "." + projectNameWithoutDash + ".controller;" + "\n" +
        "\n" +
        "import com." + creator + "." + projectNameWithoutDash + ".model." + modelName + ";" + "\n" +
        "import com." + creator + "." + projectNameWithoutDash + ".service." + modelName + "Service;" + "\n" +
        "import org.springframework.beans.factory.annotation.Autowired;" + "\n" +
        "import org.springframework.web.bind.annotation.*;" + "\n" +
        "\n" +
        "import java.util.List;" + "\n" +
        "\n" +
        "@RestController" + "\n" +
        "@RequestMapping(\"/" + modelName + "\")" + "\n" +
        "@CrossOrigin" + "\n" +
        "public class " + modelName + "Controller {" + "\n" +
        "\t@Autowired" + "\n" +
        "\tprivate " + modelName + "Service " + modelName.lower() + "Service;" + "\n" +
        "\n" +
        "\t@PostMapping(\"/add\")" + "\n" +
        "\tpublic String add(@RequestBody " + modelName + " " + modelName.lower() + ") {" + "\n" +
        "\t\t" + modelName.lower() + "Service.save" + modelName + "(" + modelName.lower() + ");" + "\n" +
        "\t\t" + "return \"New " + modelName.lower() + " is added!\";" + "\n" +
        "\t}" + "\n" +
        "\n" +
        "\t@GetMapping(\"/getAll\")" + "\n" +
        "\tpublic List<" + modelName + "> getAll" + modelName + "s() { return " + modelName.lower() + "Service.getAll" + modelName + "s(); }" + "\n" +
        "}" + "\n" 
    )

with open(path + "/repository/" + modelName + "Repository.java", "w") as repository:
    repository.write(
        "package com." + creator + "." + projectNameWithoutDash + ".repository;" + "\n" +
        "\n" +
        "import com." + creator + "." + projectNameWithoutDash + ".model." + modelName + ";" + "\n" +
        "import org.springframework.data.jpa.repository.JpaRepository;" + "\n" +
        "import org.springframework.stereotype.Repository;" + "\n" +
        "\n" +
        "@Repository" + "\n" +
        "public interface " + modelName + "Repository extends JpaRepository<" + modelName + ", Integer> {}" + "\n"
    )

with open(path + "/service/" + modelName + "Service.java", "w") as service:
    service.write(
        "package com." + creator + "." + projectNameWithoutDash + ".service;" + "\n" +
        "\n" +
        "import com." + creator + "." + projectNameWithoutDash + ".model." + modelName + ";" + "\n" +
        "\n" +
        "import java.util.List;" + "\n" +
        "\n" +
        "public interface " + modelName + "Service {" + "\n"
        "\tpublic " + modelName + " save" + modelName + "(" + modelName + " " + modelName.lower() + ");" + "\n"
        "\tpublic List<" + modelName + "> getAll" + modelName + "s();" + "\n"
        "}" + "\n"
    )    

with open(path + "/service/" + modelName + "ServiceImpl.java", "w") as controller:
    controller.write(
        "package com." + creator + "." + projectNameWithoutDash + ".service;" + "\n" +
        "\n" +
        "import com." + creator + "." + projectNameWithoutDash + ".model." + modelName + ";" + "\n" +
        "import com." + creator + "." + projectNameWithoutDash + ".repository." + modelName + "Repository;" + "\n" +
        "import org.springframework.beans.factory.annotation.Autowired;" + "\n" +
        "import org.springframework.stereotype.Service;" + "\n" +
        "\n" +
        "import java.util.List;" + "\n" +
        "\n" +
        "@Service" + "\n" +
        "public class " + modelName + "ServiceImpl implements " + modelName + "Service {" + "\n" +
        "\t@Autowired" + "\n" +
        "\tprivate " + modelName + "Repository " + modelName.lower() + "Repository;" + "\n" +
        "\n" +
        "\t@Override" + "\n" +
        "\tpublic " + modelName + " save" + modelName + "(" + modelName + " " + modelName.lower() + ") { return " + modelName.lower() + "Repository.save(" + modelName.lower() + "); }" + "\n" +
        "\t@Override" + "\n" +
        "\tpublic List<" + modelName + "> getAll" + modelName + "s() { return " + modelName.lower() + "Repository.findAll(); }" + "\n" +
        "}" + "\n" 
    )